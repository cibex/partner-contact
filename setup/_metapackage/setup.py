import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-partner-contact",
    description="Meta package for oca-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_partner_company_group>=16.0dev,<16.1dev',
        'odoo-addon-base_country_state_translatable>=16.0dev,<16.1dev',
        'odoo-addon-base_location>=16.0dev,<16.1dev',
        'odoo-addon-base_location_geonames_import>=16.0dev,<16.1dev',
        'odoo-addon-base_location_nuts>=16.0dev,<16.1dev',
        'odoo-addon-base_partner_company_group>=16.0dev,<16.1dev',
        'odoo-addon-base_partner_sequence>=16.0dev,<16.1dev',
        'odoo-addon-crm_partner_company_group>=16.0dev,<16.1dev',
        'odoo-addon-partner_accreditation>=16.0dev,<16.1dev',
        'odoo-addon-partner_address_split>=16.0dev,<16.1dev',
        'odoo-addon-partner_address_street3>=16.0dev,<16.1dev',
        'odoo-addon-partner_affiliate>=16.0dev,<16.1dev',
        'odoo-addon-partner_auto_archive>=16.0dev,<16.1dev',
        'odoo-addon-partner_bank_acc_type_constraint>=16.0dev,<16.1dev',
        'odoo-addon-partner_bank_code>=16.0dev,<16.1dev',
        'odoo-addon-partner_capital>=16.0dev,<16.1dev',
        'odoo-addon-partner_category_description>=16.0dev,<16.1dev',
        'odoo-addon-partner_category_security>=16.0dev,<16.1dev',
        'odoo-addon-partner_category_security_crm>=16.0dev,<16.1dev',
        'odoo-addon-partner_category_type>=16.0dev,<16.1dev',
        'odoo-addon-partner_company_default>=16.0dev,<16.1dev',
        'odoo-addon-partner_company_group>=16.0dev,<16.1dev',
        'odoo-addon-partner_company_type>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_access_link>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_address_default>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_age_range>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_birthdate>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_birthplace>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_department>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_gender>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_job_position>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_lang>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_nationality>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_personal_information_page>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_tags_in_popup>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_type_end_user>=16.0dev,<16.1dev',
        'odoo-addon-partner_country_state_required>=16.0dev,<16.1dev',
        'odoo-addon-partner_deduplicate_acl>=16.0dev,<16.1dev',
        'odoo-addon-partner_deduplicate_by_ref>=16.0dev,<16.1dev',
        'odoo-addon-partner_deduplicate_filter>=16.0dev,<16.1dev',
        'odoo-addon-partner_disable_gravatar>=16.0dev,<16.1dev',
        'odoo-addon-partner_display_name_line_break>=16.0dev,<16.1dev',
        'odoo-addon-partner_duns>=16.0dev,<16.1dev',
        'odoo-addon-partner_email_check>=16.0dev,<16.1dev',
        'odoo-addon-partner_email_duplicate_warn>=16.0dev,<16.1dev',
        'odoo-addon-partner_employee_quantity>=16.0dev,<16.1dev',
        'odoo-addon-partner_external_map>=16.0dev,<16.1dev',
        'odoo-addon-partner_fax>=16.0dev,<16.1dev',
        'odoo-addon-partner_firstname>=16.0dev,<16.1dev',
        'odoo-addon-partner_identification>=16.0dev,<16.1dev',
        'odoo-addon-partner_identification_eori>=16.0dev,<16.1dev',
        'odoo-addon-partner_identification_gln>=16.0dev,<16.1dev',
        'odoo-addon-partner_industry_secondary>=16.0dev,<16.1dev',
        'odoo-addon-partner_interest_group>=16.0dev,<16.1dev',
        'odoo-addon-partner_label>=16.0dev,<16.1dev',
        'odoo-addon-partner_lastname_uppercase>=16.0dev,<16.1dev',
        'odoo-addon-partner_manual_rank>=16.0dev,<16.1dev',
        'odoo-addon-partner_middlename>=16.0dev,<16.1dev',
        'odoo-addon-partner_mobile_duplicate_warn>=16.0dev,<16.1dev',
        'odoo-addon-partner_multi_relation>=16.0dev,<16.1dev',
        'odoo-addon-partner_phone_extension>=16.0dev,<16.1dev',
        'odoo-addon-partner_phonecall_schedule>=16.0dev,<16.1dev',
        'odoo-addon-partner_pricelist_search>=16.0dev,<16.1dev',
        'odoo-addon-partner_property>=16.0dev,<16.1dev',
        'odoo-addon-partner_purchase_manager>=16.0dev,<16.1dev',
        'odoo-addon-partner_ref_unique>=16.0dev,<16.1dev',
        'odoo-addon-partner_second_lastname>=16.0dev,<16.1dev',
        'odoo-addon-partner_stage>=16.0dev,<16.1dev',
        'odoo-addon-partner_subject_to_vat>=16.0dev,<16.1dev',
        'odoo-addon-partner_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-partner_tz>=16.0dev,<16.1dev',
        'odoo-addon-partner_vat_unique>=16.0dev,<16.1dev',
        'odoo-addon-purchase_supplier_rank>=16.0dev,<16.1dev',
        'odoo-addon-sale_customer_rank>=16.0dev,<16.1dev',
        'odoo-addon-sale_partner_company_group>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
